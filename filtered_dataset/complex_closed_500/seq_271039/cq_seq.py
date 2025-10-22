import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03625, 0.00038).lineTo(-0.03727, 0.00149).lineTo(-0.0521, 0.0411).lineTo(0.0521, 0.0411).lineTo(0.03725, 0.00143).lineTo(0.03638, 0.00038).lineTo(-0.03625, 0.00038).close()
solid=wp_sketch0.add(loop0).extrude(0.18581835835894567)
