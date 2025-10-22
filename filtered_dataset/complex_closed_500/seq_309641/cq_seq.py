import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 2.9845).lineTo(0.0889, 2.9845).lineTo(0.0889, 2.9464).lineTo(0.0, 2.9464).lineTo(0.0, 2.9845).close()
solid=wp_sketch0.add(loop0).extrude(-0.06086944432992718)
