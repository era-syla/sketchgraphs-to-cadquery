import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01612, 0.04843).lineTo(-0.06412, 0.04843).lineTo(-0.06412, 0.01043).lineTo(-0.01612, 0.01043).lineTo(-0.01612, 0.04843).close()
solid=wp_sketch0.add(loop0).extrude(-0.14069237687500932)
