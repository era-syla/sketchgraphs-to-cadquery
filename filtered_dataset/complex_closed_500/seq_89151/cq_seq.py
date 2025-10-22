import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03137, -0.04323).lineTo(-0.03432, -0.04508).lineTo(-0.02955, -0.05271).lineTo(-0.02659, -0.05086).lineTo(-0.03137, -0.04323).close()
solid=wp_sketch0.add(loop0).extrude(-0.01969865979174583)
