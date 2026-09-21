"""Verify evidence, hashes, retained sources and links before handoff."""
import ast,hashlib,json,re,sys
from pathlib import Path
from html.parser import HTMLParser
from PIL import Image
R=Path(__file__).resolve().parent;ROOT=R.parents[2]
read=lambda p:json.loads((R/p).read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for p in R.glob('*.py'):ast.parse(p.read_text(encoding='utf-8'))
lineage=read('lineage.json');assert sha(R/'Punching_Bag_N3_Head_Track_Yaw.blend')==lineage['successor_sha256']
assert lineage.get('parent_packet')=='reviews/2026-09-21/n3-head-track-yaw-bridge'
assert all(sha(ROOT/p)==v for p,v in lineage['baselines'].items())
assert sha(R/'SOURCE_BRIEF.md')==read('pickup.json')['brief_sha256']
for row in read('source_documents.json'):assert sha(R/row['snapshot'])==row['sha256']
assert sha(R/'assets/astronaut.png')==read('fixture_provenance.json')['sha256']
for p in ['unit_verification.json','integration_verification.json','model_verification.json','media_verification.json','usb_path_verification.json']:
    assert read(p)['status']=='PASS',p
camera=read('camera_probe.json');gym=read('gym_spotcheck.json')
assert camera['status'] in ('PRESENT','SKIPPED_NO_CAMERA'),camera
assert gym['status'] in ('GYM_DONE','SKIPPED_NO_CAMERA','SKIPPED_NO_OPERATOR_APPROVAL'),gym
if camera['status']=='SKIPPED_NO_CAMERA':
    assert gym['status']=='SKIPPED_NO_CAMERA'
assert read('integration_verification.json')['receiver_rederived'] is True
assert read('integration_verification.json')['sender_yaw_trusted'] is False
assert read('visual_review.json')['status']=='PASS_WITH_LIMITATIONS'
a=read('model_verification.json');assert a['inherited_scenes_unchanged']==5 and a['baselines_preserved']==11
assert a['fixed_bag_fill_mast_max_matrix_deviation']==a['fixed_camera_max_matrix_deviation']==0
assert a['A05_max_mm']<.01 and a['G03_sampled_proxy_min_mm']>0 and a['G05_axial_min_mm']>0
rows=read('udp_received.json');episode=[json.loads(x) for x in (R/'episode.jsonl').read_text().splitlines()]
assert len(rows)==len(episode)==144
for i,(r,p) in enumerate(zip(rows,episode)):
    assert r['seq']==p['seq']==i and r['head_centroid_x']==p['head_centroid_x']
    assert abs(r['carrier_yaw_deg']-r['output']['yaw_cmd'])<1e-4
    if i>=72:assert r['output']['yaw_cmd']==0 and not r['output']['effective_enable']
assert rows[29]['output']['yaw_cmd']<0<rows[67]['output']['yaw_cmd']
for f in R.glob('media/*.png'):
    with Image.open(f) as im:im.load();assert im.width>0
for n in ['EXECUTIVE_REVIEW','PUNCH_PATH_CHECKLIST','DEFECT_REGISTER','POSE_ATLAS','CONTINUUM_PNEUMATIC_INTENT','DOF_MECHANISM','ENVELOPE_GEOMETRY_AUDIT','INTERFACE_VULNERABILITIES','CHANGELOG_OPEN_ITEMS','TOOLCHAIN_REPRO']:
    assert (R/(n+'.md')).exists() and (R/(n+'.html')).exists()
for n in ['EXECUTIVE_REVIEW.md','READY_FOR_OLA.md']:
    body=(R/n).read_text(encoding='utf-8')
    assert all(t in body for t in ['Plain-language glossary','Track A does not prove strike impulse','B-06','C-01','SKIPPED_NO_CAMERA','live USB'])
    assert 'HY-02' in body
for f in ['packet_manifest.json','packet_verification.json']:
    if not (R/f).exists():(R/f).write_text('{}')
links=[]
class Links(HTMLParser):
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ('href','src','poster') and v and not re.match(r'^(https?:|mailto:|#)',v):links.append((self.path,v))
for f in R.glob('*.html'):
    parser=Links();parser.path=f;parser.feed(f.read_text(encoding='utf-8'))
missing=[(f.name,u) for f,u in links if not (f.parent/u.split('#')[0]).exists()]
assert not missing,missing
exclude={'packet_manifest.json','packet_verification.json','detection_preflight.jsonl'}
files=[p for p in R.rglob('*') if p.is_file() and p.name not in exclude and p.suffix not in ('.log','.tmp','.pyc') and not any(x in p.relative_to(R).parts for x in ('render_frames','composed_frames','__pycache__'))]
manifest=[dict(path=p.relative_to(R).as_posix(),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(files)]
(R/'packet_manifest.json').write_text(json.dumps(dict(pass_id=R.name,artifacts=manifest,excluded='Logs, caches, runtime latch state, detection preflight and regenerable render/composition frame sequences'),indent=2))
(R/'packet_verification.json').write_text(json.dumps(dict(
    status='PASS_WITH_ENGINEERING_RESIDUALS',
    manifest_artifacts=len(manifest),
    local_links_checked=len(links),
    missing_links=missing,
    baseline_hashes=11,
    inherited_scenes=5,
    received_frames=144,
    film_frames=144,
    key_stills=8,
    camera_probe=camera['status'],
    gym_spotcheck=gym['status'],
    source='clip fixture re-integration on inherited ACCEPTED-A successor; USB fail-fast; gym branch recorded separately',
    independent_ola_acceptance='PENDING',
    open_items=['HY-02 residual: real-gym chase not product-closed','Lead mapping / sign / idle / watchdog freeze (HY-03)','B-06/C-01 Critical hardware and propulsion','SAF-02/P-05 physical stop / limp','Loaded clearance and durability'],
    scope='Track A does not prove strike impulse. DIGITAL_TWIN_ONLY. Demo mapping remains ASSUMPTION.',
),indent=2))
print('PACKET_VERIFIED',len(manifest),'artifacts;',len(links),'local links; camera',camera['status'],'gym',gym['status'])
