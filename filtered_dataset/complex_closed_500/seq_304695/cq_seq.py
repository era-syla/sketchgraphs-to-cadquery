import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.29, 0.106).lineTo(-0.14, 0.106).lineTo(-0.16, 0.086).lineTo(-0.29, 0.086).lineTo(-0.29, 0.106).close()
solid=wp_sketch0.add(loop0).extrude(0.009636523935202932)
