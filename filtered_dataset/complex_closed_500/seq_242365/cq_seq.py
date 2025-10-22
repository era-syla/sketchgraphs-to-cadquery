import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04371, 0.0238).lineTo(0.10869, 0.0238).lineTo(0.10869, 0.0746).lineTo(0.00709, 0.0746).lineTo(0.00709, 0.1254).lineTo(-0.04371, 0.1254).lineTo(-0.04371, 0.0238).close()
solid=wp_sketch0.add(loop0).extrude(0.19791126897221675)
