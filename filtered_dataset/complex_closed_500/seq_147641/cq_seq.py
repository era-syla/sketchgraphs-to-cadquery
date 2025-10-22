import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-1.355, 0.1206).lineTo(-2.035, 0.1206).threePointArc((-2.05621, 0.12939), (-2.065, 0.1506)).lineTo(-2.065, 0.335).threePointArc((-2.05621, 0.35621), (-2.035, 0.365)).lineTo(-1.355, 0.365).threePointArc((-1.33379, 0.35621), (-1.325, 0.335)).lineTo(-1.325, 0.1506).threePointArc((-1.33379, 0.12939), (-1.355, 0.1206)).close()
solid=wp_sketch0.add(loop0).extrude(0.22748279917843386)
