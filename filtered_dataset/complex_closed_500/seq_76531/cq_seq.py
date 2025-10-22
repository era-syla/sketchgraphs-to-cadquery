import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00869, 0.03399).threePointArc((-0.01524, -0.0), (-0.00869, -0.03399)).threePointArc((-0.00658, -0.03672), (-0.00335, -0.03795)).threePointArc((0.0, -0.0381), (0.00335, -0.03795)).threePointArc((0.00658, -0.03672), (0.00869, -0.03399)).threePointArc((0.01524, 0.0), (0.00869, 0.03399)).threePointArc((0.00658, 0.03672), (0.00335, 0.03795)).threePointArc((0.0, 0.0381), (-0.00335, 0.03795)).threePointArc((-0.00658, 0.03672), (-0.00869, 0.03399)).close()
solid=wp_sketch0.add(loop0).extrude(0.21304126414094043)
