import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 1.58089).lineTo(0.4826, 1.58089).lineTo(0.4826, -0.85751).lineTo(0.0, -0.85751).lineTo(0.0, 1.58089).close()
solid=wp_sketch0.add(loop0).extrude(-4.827183193894304)
