# E — Degrees of freedom

Scene: `N3_HEAD_TRACK_YAW_BRIDGE`. Exact isolated target: `HEAD_YAW_CARRIER`, carrying `head_yaw_target = true` and N1 source identity `M1__AZ-H2__bearing_supported_arm_carrier`.

Local +Z Euler rotation supplies yaw around the mast. Home points toward world -Y; positive yaw turns toward world +X (right in the fixed front review view). ASSUMPTION: non-mirrored image right maps to this world direction; real camera alignment/sign is TBD—Lead. The live receiver owns only this target, not the bag/fill/mast or inherited scenes.

The arm geometry remains fixed in carrier coordinates. Camera is fixed. The white bag/floor datum stays still and the purple arrow turns with the carrier. Root pitch and pneumatic shape are held. The new animation uses constant key interpolation of received packets; it does not imply smooth or dynamically achievable physical motion. Reopened-model frame audit confirms the fixed and moving channels.
