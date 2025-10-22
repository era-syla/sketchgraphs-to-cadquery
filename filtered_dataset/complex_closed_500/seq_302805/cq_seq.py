import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0, 0.6604).lineTo(0.0254, 0.635).lineTo(0.0254, 0.6604).lineTo(0.0, 0.6604).close()
solid=wp_sketch0.add(loop0).extrude(0.05150064396523807)
