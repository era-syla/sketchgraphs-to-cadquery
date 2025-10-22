import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01884, 0.00889).lineTo(0.0168, 0.00889).lineTo(0.0168, -0.00408).lineTo(-0.01884, -0.00408).lineTo(-0.01884, 0.00889).close()
solid=wp_sketch0.add(loop0).extrude(0.0325555672516916)
