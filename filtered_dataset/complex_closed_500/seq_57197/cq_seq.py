import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.21591, -0.22146).lineTo(-0.21591, -0.22146).threePointArc((-0.24566, -0.20914), (-0.25798, -0.1794)).lineTo(-0.25798, 0.1794).threePointArc((-0.24566, 0.20914), (-0.21591, 0.22146)).lineTo(0.21591, 0.22146).threePointArc((0.24566, 0.20914), (0.25798, 0.1794)).lineTo(0.25798, -0.1794).threePointArc((0.24566, -0.20914), (0.21591, -0.22146)).close()
solid=wp_sketch0.add(loop0).extrude(0.9146877540399053)
