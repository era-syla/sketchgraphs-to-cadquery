import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.05523, 0.01486).lineTo(0.04379, 0.01486).lineTo(0.04379, 0.01299).lineTo(0.05523, 0.01299).lineTo(0.05523, 0.01486).close()
solid=wp_sketch0.add(loop0).extrude(0.008378084228218327)
