import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-1.43297, 0.13337).lineTo(0.59903, 0.13337).lineTo(0.59903, -0.01903).lineTo(-1.43297, -0.01903).lineTo(-1.43297, 0.13337).close()
solid=wp_sketch0.add(loop0).extrude(0.09724565187165458)
