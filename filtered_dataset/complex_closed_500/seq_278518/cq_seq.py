import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, -0.01237).threePointArc((-0.01237, -0.0), (0.0, 0.01237)).lineTo(0.0, -0.01237).close()
solid=wp_sketch0.add(loop0).extrude(0.05118852226450036)
