import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0055, -0.041).lineTo(0.0335, -0.041).lineTo(0.0335, -0.0355).threePointArc((0.03511, -0.03161), (0.039, -0.03)).lineTo(0.0613, -0.03).lineTo(0.0613, -0.0258).lineTo(0.0505, -0.015).lineTo(0.0, -0.015).lineTo(0.0, -0.0253).lineTo(0.0055, -0.0308).lineTo(0.0055, -0.041).close()
solid=wp_sketch0.add(loop0).extrude(0.17720861072316588)
