import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0085, 0.222).lineTo(0.2135, 0.222).lineTo(0.2135, 0.0085).lineTo(0.0085, 0.0085).lineTo(0.0085, 0.222).close()
solid=wp_sketch0.add(loop0).extrude(-0.39694197438407847)
