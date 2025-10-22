import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01, -0.025).lineTo(-0.01, -0.025).threePointArc((-0.02061, -0.02061), (-0.025, -0.01)).lineTo(-0.025, 0.01).threePointArc((-0.02061, 0.02061), (-0.01, 0.025)).lineTo(0.01, 0.025).threePointArc((0.02061, 0.02061), (0.025, 0.01)).lineTo(0.025, -0.01).threePointArc((0.02061, -0.02061), (0.01, -0.025)).close()
solid=wp_sketch0.add(loop0).extrude(0.11904812173927908)
