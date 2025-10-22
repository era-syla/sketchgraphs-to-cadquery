import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.1285, 0.09103).lineTo(0.11725, 0.08675).lineTo(0.11143, 0.10672).lineTo(0.12295, 0.11008).lineTo(0.1285, 0.09103).close()
solid=wp_sketch0.add(loop0).extrude(-0.047246750857701386)
