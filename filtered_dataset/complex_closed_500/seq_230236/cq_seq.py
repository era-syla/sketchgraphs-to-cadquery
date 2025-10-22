import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.25349, 0.10612).lineTo(0.21574, 0.05252).lineTo(0.10058, 0.20918).lineTo(-0.25349, 0.10612).close()
solid=wp_sketch0.add(loop0).extrude(0.29256966485083)
