import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-1.3843, 0.1651).lineTo(-1.3843, -0.1651).lineTo(-0.5334, -0.2413).lineTo(0.508, -0.2413).lineTo(0.508, 0.2413).lineTo(-0.5334, 0.2413).lineTo(-1.3843, 0.1651).close()
solid=wp_sketch0.add(loop0).extrude(-1.0092999297415974)
