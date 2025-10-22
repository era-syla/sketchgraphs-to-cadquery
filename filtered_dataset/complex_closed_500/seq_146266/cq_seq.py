import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-1.469, 0.487).lineTo(-1.453, 0.487).lineTo(-1.453, 0.427).lineTo(-1.469, 0.427).lineTo(-1.469, 0.487).close()
solid=wp_sketch0.add(loop0).extrude(-0.04104511215378915)
