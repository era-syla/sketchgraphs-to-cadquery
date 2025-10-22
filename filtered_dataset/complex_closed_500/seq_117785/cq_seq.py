import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.782, 0.722).lineTo(-0.018, 0.722).lineTo(-0.018, 0.612).lineTo(-0.782, 0.612).lineTo(-0.782, 0.722).close()
solid=wp_sketch0.add(loop0).extrude(-1.61861157937537)
