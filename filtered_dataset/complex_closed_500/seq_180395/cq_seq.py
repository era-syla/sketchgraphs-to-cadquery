import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0762, -0.02554).lineTo(0.0254, -0.02554).lineTo(0.0254, 0.05066).lineTo(0.0, 0.05066).lineTo(0.0, 0.01256).lineTo(-0.0508, 0.01256).lineTo(-0.0508, 0.05066).lineTo(-0.0762, 0.05066).lineTo(-0.0762, -0.02554).close()
solid=wp_sketch0.add(loop0).extrude(-0.25764539885020893)
