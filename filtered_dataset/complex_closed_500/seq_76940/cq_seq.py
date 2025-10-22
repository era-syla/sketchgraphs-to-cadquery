import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0015, 0.001).threePointArc((-0.0, 0.0025), (-0.0015, 0.001)).lineTo(-0.0015, 0.0).lineTo(-0.004, 0.0).lineTo(-0.004, 0.001).threePointArc((-0.0, 0.005), (0.004, 0.001)).lineTo(0.004, 0.0).lineTo(0.0015, 0.0).lineTo(0.0015, 0.001).close()
solid=wp_sketch0.add(loop0).extrude(0.01096682177060697)
