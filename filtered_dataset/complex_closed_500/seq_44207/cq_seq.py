import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05553, 0.0962).lineTo(-0.05803, 0.0962).lineTo(-0.05803, 0.0112).lineTo(-0.05553, 0.0112).lineTo(-0.05553, 0.0962).close()
solid=wp_sketch0.add(loop0).extrude(0.21436856570874302)
