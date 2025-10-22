import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 2.0).threePointArc((0.04464, 2.10776), (0.1524, 2.1524)).lineTo(1.6524, 2.1524).threePointArc((1.76016, 2.10776), (1.8048, 2.0)).lineTo(1.8048, 0.0).threePointArc((1.76016, -0.10776), (1.6524, -0.1524)).lineTo(0.1524, -0.1524).threePointArc((0.04464, -0.10776), (0.0, -0.0)).close()
solid=wp_sketch0.add(loop0).extrude(4.490580512803084)
