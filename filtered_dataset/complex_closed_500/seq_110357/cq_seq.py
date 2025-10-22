import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03262, -0.00635).lineTo(0.06898, -0.00635).lineTo(0.06898, 0.00635).lineTo(-0.03262, 0.00635).lineTo(-0.03262, -0.00635).close()
solid=wp_sketch0.add(loop0).extrude(0.2770813358637509)
