import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0325, -0.16225).lineTo(0.0325, -0.16225).lineTo(0.0325, -0.16375).lineTo(-0.0325, -0.16375).lineTo(-0.0325, -0.16225).close()
solid=wp_sketch0.add(loop0).extrude(-0.046677074649328895)
