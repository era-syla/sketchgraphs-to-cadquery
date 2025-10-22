import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.10774, 0.232).lineTo(-0.01226, 0.232).lineTo(-0.01226, 0.592).lineTo(0.10774, 0.592).lineTo(0.10774, 0.232).close()
solid=wp_sketch0.add(loop0).extrude(-0.1717217839104668)
