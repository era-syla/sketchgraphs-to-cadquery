import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.028).lineTo(0.0, 0.093).lineTo(-0.00632, 0.093).threePointArc((-0.01745, 0.08619), (-0.02182, 0.07389)).lineTo(-0.02182, 0.028).lineTo(-0.0, 0.028).close()
solid=wp_sketch0.add(loop0).extrude(-0.010701410424925095)
