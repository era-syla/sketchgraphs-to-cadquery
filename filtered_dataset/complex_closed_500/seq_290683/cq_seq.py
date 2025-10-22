import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.012, 0.045).lineTo(0.018, 0.045).lineTo(0.018, 0.033).lineTo(-0.012, 0.033).lineTo(-0.012, 0.045).close()
solid=wp_sketch0.add(loop0).extrude(0.057578222833544614)
