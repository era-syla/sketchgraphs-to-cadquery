import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.11949, -0.02843).lineTo(-0.07549, -0.02843).lineTo(-0.07549, -0.05643).lineTo(-0.11949, -0.05643).lineTo(-0.11949, -0.02843).close()
solid=wp_sketch0.add(loop0).extrude(-0.04549006756124782)
