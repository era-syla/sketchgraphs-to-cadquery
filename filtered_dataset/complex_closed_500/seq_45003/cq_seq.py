import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0024, 0.00658).threePointArc((-0.0135, -0.0), (-0.0024, -0.00658)).threePointArc((0.0, -0.00597), (0.0024, -0.00658)).threePointArc((0.0135, 0.0), (0.0024, 0.00658)).threePointArc((-0.0, 0.00597), (-0.0024, 0.00658)).close()
solid=wp_sketch0.add(loop0).extrude(0.06622025714193505)
