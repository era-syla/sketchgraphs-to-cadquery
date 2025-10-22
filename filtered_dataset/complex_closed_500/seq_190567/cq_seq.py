import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00055, -0.01224).lineTo(-0.01169, -0.03307).lineTo(-0.03252, -0.02083).lineTo(-0.02028, 0.0).lineTo(0.00055, -0.01224).close()
solid=wp_sketch0.add(loop0).extrude(-0.0013756152030112256)
