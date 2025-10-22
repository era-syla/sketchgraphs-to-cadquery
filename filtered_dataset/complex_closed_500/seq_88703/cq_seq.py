import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03403, -0.08638).lineTo(-0.04903, -0.08638).lineTo(-0.04903, 0.00381).lineTo(-0.03403, 0.00381).lineTo(-0.03403, -0.08638).close()
solid=wp_sketch0.add(loop0).extrude(-0.10503221409675786)
