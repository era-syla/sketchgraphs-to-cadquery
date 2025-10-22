import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-3.69022, 1.7399).lineTo(-3.77912, 1.7399).lineTo(-3.77912, -1.7399).lineTo(-3.69022, -1.7399).lineTo(-3.69022, 1.7399).close()
solid=wp_sketch0.add(loop0).extrude(-9.310974061896463)
