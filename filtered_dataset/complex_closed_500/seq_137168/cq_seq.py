import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04558, 0.05153).lineTo(-0.03613, 0.05153).lineTo(-0.03613, 0.03674).lineTo(-0.04558, 0.03674).lineTo(-0.04558, 0.05153).close()
solid=wp_sketch0.add(loop0).extrude(0.019489977771482547)
