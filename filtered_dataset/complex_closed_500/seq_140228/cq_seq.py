import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.23459, -0.03056).lineTo(-0.18305, -0.03056).lineTo(-0.18305, -0.16307).lineTo(-0.23459, -0.16307).lineTo(-0.23459, -0.03056).close()
solid=wp_sketch0.add(loop0).extrude(0.2109919334939884)
