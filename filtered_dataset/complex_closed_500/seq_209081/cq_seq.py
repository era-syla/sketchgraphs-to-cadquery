import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-1.46603, 17.156).threePointArc((-1.46603, 16.156), (-0.6, 15.656)).lineTo(-0.6, 16.656).lineTo(-1.46603, 17.156).close()
solid=wp_sketch0.add(loop0).extrude(3.9459651632160466)
