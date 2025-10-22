import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.34925, 0.508).lineTo(-0.15875, 0.508).lineTo(-0.15875, 0.0).lineTo(-0.34925, 0.0).lineTo(-0.34925, 0.508).close()
solid=wp_sketch0.add(loop0).extrude(0.3627880566537064)
