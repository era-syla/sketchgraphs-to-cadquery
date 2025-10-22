import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.16851, 0.13225).lineTo(0.16251, 0.13225).threePointArc((0.16604, 0.13079), (0.16751, 0.12725)).lineTo(0.16751, -0.12668).threePointArc((0.16604, -0.13021), (0.16251, -0.13168)).lineTo(-0.16851, -0.13168).threePointArc((-0.17204, -0.13021), (-0.17351, -0.12668)).lineTo(-0.17351, 0.12725).threePointArc((-0.17204, 0.13079), (-0.16851, 0.13225)).close()
solid=wp_sketch0.add(loop0).extrude(-0.14862702128478333)
