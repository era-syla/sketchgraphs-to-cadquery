import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0105, -0.004).lineTo(0.0155, -0.004).lineTo(0.0155, -0.002).lineTo(-0.0105, -0.002).lineTo(-0.0105, -0.004).close()
solid=wp_sketch0.add(loop0).extrude(-0.07309706165262826)
