import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03866, -0.02299).lineTo(0.02548, -0.02299).lineTo(0.02548, -0.0388).lineTo(-0.03866, -0.0388).lineTo(-0.03866, -0.02299).close()
solid=wp_sketch0.add(loop0).extrude(-0.06964641654570705)
