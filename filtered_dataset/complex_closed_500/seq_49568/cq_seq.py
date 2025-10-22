import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.08723, -0.35587).lineTo(0.58758, -0.35587).lineTo(0.58758, 0.35587).lineTo(-0.08723, 0.35587).lineTo(-0.08723, -0.35587).close()
solid=wp_sketch0.add(loop0).extrude(-2.050635476146778)
