import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.10727, -0.09299).lineTo(-0.09663, -0.09299).lineTo(-0.09663, -0.0102).lineTo(-0.10727, -0.0102).lineTo(-0.10727, -0.09299).close()
solid=wp_sketch0.add(loop0).extrude(0.02856633171164485)
