import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00125, 0.0523).lineTo(0.00125, 0.0523).lineTo(0.00125, 0.0508).lineTo(-0.00125, 0.0508).lineTo(-0.00125, 0.0523).close()
solid=wp_sketch0.add(loop0).extrude(0.004087352852540293)
