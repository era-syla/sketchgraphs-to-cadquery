import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00795, 0.00505).lineTo(-0.01078, 0.00222).lineTo(-0.00512, -0.00344).lineTo(-0.00229, -0.00061).lineTo(-0.00795, 0.00505).close()
solid=wp_sketch0.add(loop0).extrude(0.022973699329118545)
