import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0381, 0.00318).lineTo(0.0508, 0.00318).lineTo(0.0508, -0.00389).lineTo(0.0381, -0.00389).lineTo(0.0381, 0.00318).close()
solid=wp_sketch0.add(loop0).extrude(0.008085319180928367)
