import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.116, 0.0185).lineTo(0.166, 0.0185).lineTo(0.166, 0.0085).lineTo(0.116, 0.0085).lineTo(0.116, 0.0185).close()
solid=wp_sketch0.add(loop0).extrude(0.12454946866074623)
