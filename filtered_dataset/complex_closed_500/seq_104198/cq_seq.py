import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.14092, 0.46094).lineTo(-0.13361, 0.43703).lineTo(-0.15274, 0.43118).lineTo(-0.16005, 0.45509).lineTo(-0.14092, 0.46094).close()
solid=wp_sketch0.add(loop0).extrude(0.041211353520350165)
