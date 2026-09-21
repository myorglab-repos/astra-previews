# E — Degrees of freedom

Scene: `N3_HEAD_TRACK_YAW_BRIDGE` (inherited ACCEPTED-A successor). Exact isolated target: `HEAD_YAW_CARRIER`, carrying `head_yaw_target = true` and N1 source identity `M1__AZ-H2__bearing_supported_arm_carrier`.

Local +Z Euler rotation supplies yaw around the mast. Home points toward world -Y; positive yaw turns toward world +X (right in the fixed front review view). ASSUMPTION: non-mirrored image right maps to this world direction; real camera alignment/sign is TBD—Lead.

The live USB sender uses the same mapping. Idle policy remains **home_zero**. This pass does not remake carrier keys.
