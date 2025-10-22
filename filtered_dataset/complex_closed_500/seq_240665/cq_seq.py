import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00422, 0.0215).lineTo(0.00422, 0.0215).threePointArc((0.0, 0.00725), (-0.00422, 0.0215)).close()
solid=wp_sketch0.add(loop0).extrude(-0.041782220717356426)
