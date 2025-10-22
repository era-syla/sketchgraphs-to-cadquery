import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0007, 0.09299).lineTo(-0.0007, 0.05799).threePointArc((0.00223, 0.05091), (0.0093, 0.04799)).lineTo(0.0243, 0.04799).threePointArc((0.0314, 0.04571), (0.03586, 0.03974)).lineTo(0.04116, 0.02435).lineTo(0.03727, 0.02335).lineTo(0.03197, 0.03874).threePointArc((0.02979, 0.04167), (0.0263, 0.04279)).lineTo(0.0113, 0.04279).threePointArc((0.00055, 0.04724), (-0.0039, 0.05799)).lineTo(-0.0039, 0.09299).lineTo(-0.0007, 0.09299).close()
solid=wp_sketch0.add(loop0).extrude(0.11818666638006631)
